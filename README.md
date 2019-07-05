# gRPC Example

This is an example project that uses gRPC.

To generate the source code for the C# gRPC server, use the following command.

```PowerShell
protoc -I .\pb\ --csharp_out .\logging-grpc-server\Messages\ .\pb\Log.proto --grpc_out .\logging-grpc-server\Messages\ --plugin=protoc-gen-grpc=C:\Users\mikey\.nuget\packages\grpc.tools\1.21.0\tools\windows_x64\grpc_csharp_plugin.exe
```

python -m grpc_tools.protoc -I .\pb\ --python_out=.\logging-grpc-client\ --grpc_python_out=.\logging-grpc-client\ .\pb\Log.proto