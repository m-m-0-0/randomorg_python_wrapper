# randomorg_python_wrapper
A simple Python wrapper around api.random.org

##Requirements
* Requests

##Usage

>\>\>\>import Randomorg

>\>\>\>r = Randomorg('00000000-0000-0000-0000-000000000000')

>\>\>\>r.status()

>running

>\>\>\>r.bitsLeft()

>990938

>\>\>\>r.requestsLeft()

>199973

>\>\>\>r.generateIntegers(10,0,1000)

>[745, 870, 561, 19, 298, 467, 446, 24, 122, 136]

>\>\>\>r.generateGaussians(10,1,1,5)

>[-1.1889, 1.3311, 0.49156, 2.2397, -0.2477, 1.2216, 2.1675, 2.0453, 0.38347, 0.55488]

>\>\>\>r.generateStrings(10,10,'abcdefghijklmnopqrstuvwxyz',replacement='false')

>['dejiptanec', 'vrkkkcwtbq', 'dzjdskmzfp', 'xilyltmwlt', 'cungdmqgxw', 'pzadwzfcjm', 'clvquwikyf', 'gpmzkrepbr', 'xczmirvnem', 'inuvusydbq']

>\>\>\>r.generateUUIDs(10)

>['4f5e1d3b-5661-47ba-8a0b-06f4a09c457e', '1897ddd0-dea1-42c8-92e1-c9e4a541ddab', '9e4ebea6-bdb3-4c84-824a-acf4e1512129', 'cd5c28e7-d0e3-44a9-b857-396388f9e525', '0fb94394-36c9-444c-880d-3bade42ca973', 'e3ea567a-3af5-417c-a973-9d7f5b33a269'>, '1180478f-82d1-4efc-b014-d297dcef6714', '797a2f47-f0d6-40eb-9eae-1abd32c684a7', 'c106ce40-2348-4fd8-8859-dc617af96f8d', 'db740810-bdd0-4c80-8d15-2b11a7decb1c']

>\>\>\>r.generateBlobs(2,128,format='base64')

>['S0LztOot8Xp0JQousbZGSA==', 'fk1JhS2lgdSMrr81LIv6sQ==']
