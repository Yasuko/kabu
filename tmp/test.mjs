#!/usr/bin/env zx
const result = await $`ls -la`
console.log(result) // stdout, stderr, exitCodeなどが取得できる