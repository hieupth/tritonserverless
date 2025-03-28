import runpod
import trism


async def async_generator_handler(job):

    try:
        client = get_client(job['model_metadata'], job['is_llm'])
        async for response in client.run(job): # list of responses
            yield response
    except Exception as e:
        return {"error": str(e)}
    
    
def get_client(model_metadata: dict, is_llm: bool = False):

    client = trism.TritonModel(
        model=model_metadata['model'],
        version=model_metadata['version'],
        url=model_metadata['url'],
        grpc=model_metadata['grpc']
    )
    return client


if __name__ == "__main__":

    runpod.serverless.start(
        {
            "handler": async_generator_handler,  # Required: Specify the async handler
            "return_aggregate_stream": True,  # Optional: Aggregate results are accessible via /run endpoint
        }
    )
