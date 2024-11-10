// place files you want to import through the `$lib` alias in this folder.

export async function PostApi(endpoint: string, body: object): Promise<Response>  {
    const res = await fetch(endpoint, {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(body)
    });
    return await res;
}


export async function PostApiPing(text: string): Promise<string> {
    const res = await PostApi("api/record", {
        text
    });
    const json = await res.json();
    return JSON.stringify(json);
}