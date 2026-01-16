import { useEffect, useState } from "react";
import { CatItem } from "./cat-item";

export function CatsList() {
    const [items, setItems] = useState([])

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await fetch("http://127.0.0.1:8000/cats/");
                const data = await res.json();
                setItems(data);
            } catch (error) {
                console.error("Error while getting cats", error);
            }
        };

        fetchData();
    }, [])

    return (
        <ul className="flex flex-col gap-1 px-5">
            {
                items.map((item) => (
                    <CatItem key={item.id} name={item.name} years={item.years_of_experience} breed={item.breed} salary={item.salary} />
                ))
            }
        </ul>
    )
}