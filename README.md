# gRPC Example

This is an example project that uses gRPC

```PowerShell
protoc -I .\pb\ `
    --csharp_out .\logging-grpc-server\Messages\ `
    --grpc_out .\logging-grpc-server\Messages\ `
    --plugin=protoc-gen-grpc=C:\Users\mikey\.nuget\packages\grpc.tools\1.21.0\tools\windows_x64\grpc_csharp_plugin.exe `
    .\pb\Log.proto
```