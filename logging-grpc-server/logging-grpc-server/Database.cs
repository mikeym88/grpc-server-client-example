using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace logging_grpc_server
{
    public class InMemoryDb
    {
        private static List<Messages.Log> inMemoryDb = null;
        private static InMemoryDb _instance = null;

        protected InMemoryDb()
        {
            // Exists only to defeat instantiation.
            inMemoryDb = new List<Messages.Log>();
        }

        public static InMemoryDb GetInstance()
        {
            if (_instance == null)
            {
                _instance = new InMemoryDb();
            }
            return _instance;
        }

        public Task<Guid> LogAsync(string message, string logType)
        {
            Guid g = Guid.NewGuid();
            lock (inMemoryDb)
            {
                inMemoryDb.Add(new Messages.Log()
                {
                    Guid = g.ToString(),
                    Message = message,
                    Type = logType
                });
            }

            return Task.FromResult(g);
        }

        // https://stackoverflow.com/a/13254787/6288413
        public Task<Messages.Log> GetLog(Guid g)
        {
            foreach (var entry in inMemoryDb)
            {
                if (entry.Guid.Equals(g.ToString()))
                {
                    return Task.FromResult(entry);
                }
            }
            throw new Exception($"Log not found with GuID {g.ToString()}.");
        }
    }
}
