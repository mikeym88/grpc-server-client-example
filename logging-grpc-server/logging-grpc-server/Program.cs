using Grpc.Core;
using Messages;
using System;
using System.Threading.Tasks;
using static Messages.LogService;

namespace logging_grpc_server
{
    class Program
    {
        static InMemoryDb db = InMemoryDb.GetInstance();
        static void Main(string[] args)
        {
            Console.WriteLine("Starting logging service.");
            const int Port = 9000;

            Server server = new Server
            {
                Ports = { new ServerPort("0.0.0.0", Port, ServerCredentials.Insecure) },
                Services = { BindService(new LogService()) }
            };
            server.Start();

            Console.WriteLine($"Starting server on port {Port}");
            Console.WriteLine("Press any key to stop...");
            Console.ReadKey();

            server.ShutdownAsync().Wait();
        }

        public class LogService : LogServiceBase
        {
            public override async Task<LogResponse> Log(LogRequest request, ServerCallContext context)
            {
                Console.WriteLine($"Adding Log of Type {request.Log.Type.ToString()}: {request.Log.Message}");
                Guid g = await db.LogAsync(request.Log.Message, request.Log.Type.ToString());
                Console.WriteLine($"Logged successully: {g}");
                return new LogResponse()
                {
                    Guid = g.ToString()
                };
            }

            public override async Task<GetLogResponse> GetLog(GetLogRequest request, ServerCallContext context)
            {
                Metadata md = context.RequestHeaders;
                foreach (var entry in md)
                {
                    Console.WriteLine(entry.Key + ": " + entry.Value);
                }
                var mes = await db.GetLog(Guid.Parse(request.Guid));
                return new GetLogResponse()
                {
                    Log = mes
                };
            }
        }
    }
}
