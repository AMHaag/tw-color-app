import Image from "next/image";
import full_logo from "../../assets/Full-Logo.png";
import Link from "next/link";

function Header() {
  return (
    <header className="header py-02 sticky top-0 w-screen items-center justify-between bg-jcb-950 px-8 md:flex">
      <Link href="/">
        <div id="header_logo" className="">
          <Image src={full_logo} width={250} height={80} alt="Logo" />
        </div>
      </Link>
      <div></div>
      <nav className="nav text-xl font-light">
        <ul className="flex items-center">
          <li className="active cursor-pointer border-b-2 border-jcb-400 border-opacity-0 p-4 text-sm text-jcb-50 duration-200 hover:border-opacity-100 hover:font-semibold hover:text-jcb-200 md:text-base">
            <Link href="/">Home</Link>
          </li>
          <li className="cursor-pointer border-b-2 border-jcb-400 border-opacity-0 p-4 text-sm text-jcb-50 duration-200 hover:border-opacity-100 hover:font-semibold hover:text-jcb-200 md:text-base">
            <Link href="/faq">FAQ</Link>
          </li>
          <li className="cursor-pointer border-b-2 border-jcb-400 border-opacity-0 p-4 text-sm text-jcb-50 duration-200 hover:border-opacity-100 hover:font-semibold hover:text-jcb-200 md:text-base">
            <Link href="/support">Support</Link>
          </li>
          <li className="cursor-pointer border-b-2 border-jcb-400 border-opacity-0 p-4 text-sm text-jcb-50 duration-200 hover:border-opacity-100 hover:font-semibold hover:text-jcb-200 md:text-base">
            <Link href="/contribute">Contribute</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
