from typing import List

from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"                    # Values: "global"
# search_engine_id = "YOUR_SEARCH_ENGINE_ID"
# serving_config_id = "default_config"          # Values: "default_config"
# search_query = "YOUR_SEARCH_QUERY"


def search_sample(
    project_id: str,
    location: str,
    search_engine_id: str,
    serving_config_id: str,
    search_query: str,
) -> List[discoveryengine.SearchResponse.SearchResult]:
    # Create a client
    client = discoveryengine.SearchServiceClient()

    # The full resource name of the search engine serving config
    # e.g. projects/{project_id}/locations/{location}
    serving_config = client.serving_config_path(
        project=project_id,
        location=location,
        data_store=search_engine_id,
        serving_config=serving_config_id,
    )

    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=search_query,
    )
    response = client.search(request)
    for result in response.results:
        print(result)

    return response.results
search_sample("ucs-fishfood-5", "global", "rick-chen-unstructured_1682736499332",
              "default_config","Where is Youtube studio"
              )