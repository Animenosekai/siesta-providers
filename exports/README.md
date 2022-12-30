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
