# Alvaro-Germans

## Introduction

I'm not very good at anagrams, so I've decided to write my own anagram solver. Now, as long as I have access to my laptop, I'll be able to impress my friends.



## Milestones

* Solve one-word anagrams
* Solve multi-word anagrams
* Build a front end so I can do it sneaky-like.

## Intuition

Any two anagrams can be compared in two sorting operations,

```
acb -> abc
cba -> abc
=> acb is an anagram of cba
```

Therefore, each dictionary word can be expressed by the following map,

```
F: anagram --> word
F(aelpp) = apple
F(aaabnn) = banana
```

Step one is building the map.