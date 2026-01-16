export function CatItem({ name, years, breed, salary }) {
    return (
        <li className="border-2 border-b-gray-600 h-8 text-[20px] flex justify-between items-center px-2">
            <span>{name}</span>
            <span>{years}</span>
            <span>{breed}</span>
            <span>{salary}</span>
        </li>
    )
}