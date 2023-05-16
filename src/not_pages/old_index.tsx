import { type NextPage } from "next";
import Head from "next/head";
//import Link from "next/link";
import Header from '../components/header'
import { api } from "~/utils/api";

const Home: NextPage = () => {
	const hello = api.example.hello.useQuery({ text: "from tRPC" });
	return (

		<>
			<Head>
				<title>TW Colorized</title>
				<meta name="description" content="A general tool to create Tailwind Color Palletes" />
				<link rel="icon" href="/favicon.ico" />
			</Head>
			<Header />
			<main>
				Test
			</main>
		</>
	);
};

export default Home;
