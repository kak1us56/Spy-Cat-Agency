import Head from "next/head";
import { Main } from "../components/main/main";

export default function HomePage() {

  return (
    <>
        <Head>
            <title>Spy Cat Agency</title>
        </Head>
        <div>
            <Main />
        </div>
    </>
  );
}
