#!/usr/bin/env zx


const all = await ps.lookup()
const nodejs = await ps.lookup({ command: 'node' })
const children = await ps.tree({ pid: 123 })
const fulltree = await ps.tree({ pid: 123, recursive: true })

console.log(all)
console.log(nodejs)
console.log(children)
console.log(fulltree)