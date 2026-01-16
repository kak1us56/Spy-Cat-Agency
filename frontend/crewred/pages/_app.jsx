import "../styles/global.css";
import { Montserrat } from "next/font/google";

const montserrat = Montserrat({
  subsets: ["latin", "cyrillic"],
});


export default function App({ Component, pageProps }) {
    return (
        <div className={montserrat.className}>
            <Component {...pageProps} />
        </div>
    )
}
