import { postcss } from "tailwindcss"

export default async function Temperaturas() {

    const response = await fetch('http://localhost:3000/temperaturas')
    const data = await response.json()

    return (
        <>
            {data.map((item: any) => <li key={item.posts.id}>{item.post.title}</li>)}
        </>
    )
}