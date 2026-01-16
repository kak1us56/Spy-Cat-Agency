import { CatsList } from "./cats-list";

export function Main() {
    return (
        <main>
            <h1 className="text-4xl font-bold text-blue-600 mb-4 text-center">Spy Cat Agency</h1>
            <div>
                <CatsList />
            </div>
        </main>
    )
}