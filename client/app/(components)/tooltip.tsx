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
                whitespace-nowrap
                rounded
                bg-black
                px-2
                py-1
                text-white
                absolute
                "
            >
                { tips }
            </div>
            <div
                className="
                    z-50
                    rounded px-0 py-1
                    shadow  hover:bg-gray-100
                    cursor-pointer"
                onClick={() => setShow(true)}
                onMouseLeave={() => setShow(false)}>
                { label }
            </div>
        </>
    )
}