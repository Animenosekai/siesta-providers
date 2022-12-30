# exports

This directory is holding the various files exported to the internet.

## Search

The search feature on the market webpage uses [`search.json`](search.json)

This is a file containing tokens to match queries:

```typescript
interface SearchFile {
    [key: string]: SearchToken
}

interface SearchToken {
    i: string // the id
    t: "a" | "p" // type, "a" for "author" and "p" for "provider"
}
```


<!-- 
## Listings

We use different files to list and cache the informations on the exported providers.

This is used by the market pages to avoid querying recursively for all of the data.

```typescript
interface Listing {
    i: string // id
    n: string // name
    d: string // description
    t: ProviderType
}

interface ProviderType {
    t: 0 | 1 // tv
    m: 0 | 1 // media
    µ: 0 | 1 // metadata
}
``` -->
