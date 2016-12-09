# -*- coding: utf-8 -*-
'''
use Microsoft Entity Link API to extract entities from scientific papers.
'''
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'text/plain',
    'Ocp-Apim-Subscription-Key': '2b3ce8d8300a4eeea41e628c3f214301',
}

params = urllib.urlencode({
    # Request parameters
    #'selection': '{string}',
    #'offset': '{string}',
})

body_text = '''
From the results in Figure 4 we can see that in the NIPS collection, NTSeg performs better than the comparative methods especially when the number of segment-topics is 10. However, its performance deteriorates a bit when the number of segment-topics is increased, but still remains competitive with the comparative methods. Moreover, we notice that as the number of word-topics increases, the performance of NTSeg deteriorates to some extent in the NIPS collection. However, in the OHSUMED collection, NTSeg again performs better against the comparative methods when the number of word-topics is increased. We can observe that NTSeg outperforms the comparative methods considerably when the number of segment-topics is 100. The results suggest that NTSeg can perform very well on large document collections as large collections provide richer information about word co-occurrences.'''

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/entitylinking/v1.0/link?%s" % params, body_text, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))