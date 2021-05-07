import json
import requests


__enrichmentAnalysis_ENRICHR_URL = 'http://maayanlab.cloud/Enrichr/'

def getEnrichment(geneList, gene_set_library = 'GO_Biological_Process_2018'):
    genes_str = '\n'.join(geneList)
    description = 'Genes to analyze'
    payload = {
        'list': (None, genes_str),
        'description': (None, description)
    }

    response = requests.post(__enrichmentAnalysis_ENRICHR_URL + 'addList', files=payload)
    if not response.ok:
        raise Exception('Error analyzing gene list')

    user_list_info = json.loads(response.text)

    query_string = '?userListId=%s&backgroundType=%s'
    user_list_id = user_list_info['userListId']

    response = requests.get(
        __enrichmentAnalysis_ENRICHR_URL + 'enrich' + query_string % (user_list_id, gene_set_library)
    )
    if not response.ok:
        raise Exception('Error fetching enrichment results')

    print("Order of returned results is: Rank, Term name, P-value, Z-score, Combined score, Overlapping genes, "
          "Adjusted p-value, Old p-value, Old adjusted p-value")

    return json.loads(response.text)