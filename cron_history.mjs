#!/usr/bin/env zx


// パトロール実行関数
const runPatroll = async () => {
    try {
        const output = await $`docker exec ${pythonContainer.id} python /root/work/patrol.py`
        return {
            status: true,
            message: output
        }
    } catch (error) {
        return {
            status: false,
            message: error
        }
    }
}

// sleep関数
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms))





// 実行中のDockerコンテナの一覧を取得
const { stdout } = await $`docker ps --format "{{.ID}} {{.Names}}"`

// 結果を整形
const _s = stdout.trim().split('\n').map((line) => {
        const [id, name] = line.split(' ')
        return { id, name }
    })

// pythonコンテナのIDを取得
const pythonContainer = _s.find((x) => x.name.includes('python'))

console.log(pythonContainer)

// pythonコンテナが存在する場合、巡回実行
if (pythonContainer) {
    try {
        const output = await runPatroll()
        console.log(output)
    } catch (error) {
        console.log(error)
        sleep(1800000)
        const output = await runPatroll()
        console.log(output)
    }
}

