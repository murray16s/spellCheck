#! /usr/bin/env python3
import marisa_trie
tr = marisa_trie.Trie([u'cows', u'pig', u'cop'])
tr2 = marisa_trie.Trie(['cows', 'pig', 'cop'])
print('cow' in tr)
print('cows' in tr)
