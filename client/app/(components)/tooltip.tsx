import React from "react"

export default function ToolTip({
    label,
    tips,
    position = "top",
}: {
    label: string,
    tips: string,
    position: "top" | "bottom" | "left" | "right",
}) {
    const [show, setShow] = React.useState(false)

    return (
        <>
            <div
                hidden={show ? false : true}
                className="
                z-[1000] absolute left-[200px] px-2 py-1 mt-[-50px]
                w-[500px] h-[600px] text-left
                text-white
                whitespace-normal rounded
                bg-black
                "
            >
                <pre>{ tips }</pre>
            </div>
            <div
                className="
                    z-50
                    rounded px-0 py-1
                    shadow  hover:bg-gray-600
                    cursor-pointer"
                onMouseOver={() => setShow(true)}
                onMouseOut={() => setShow(false)}>
                { label }
            </div>
        </>
    )
}