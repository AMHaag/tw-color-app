import Image from 'next/image'
import full_logo from '../assets/Full-Logo.png'


function Header() {
	return (
		<header className='header sticky top-0 shadow-md flex items-center justify-between px-8 py-02 bg-jcb-950 w-screen'>
			<div id='header_logo' className=''>
				<Image
					src={full_logo}
					width={250}
					height={80}
					alt='Logo'
				/>
			</div>
			<div>

			</div>
			<nav className="nav font-semibold text-xl font-light">
				<ul class="flex items-center">
					<li class="p-4 text-jcb-50 border-b-2 border-jcb-400 border-opacity-0 hover:border-opacity-100 hover:text-jcb-200 duration-200 cursor-pointer active">
						<a href="">Home</a>
					</li>
					<li class="p-4 text-jcb-50 border-b-2 border-jcb-400 border-opacity-0 hover:border-opacity-100 hover:text-jcb-200 duration-200 cursor-pointer">
						<a href="">FAQ</a>
					</li>
					<li className="p-4 text-jcb-50 border-b-2 border-jcb-400 border-opacity-0 hover:border-opacity-100 hover:text-jcb-200 duration-200 cursor-pointer">
						<a href="">Support</a>
					</li>
					<li className="p-4 text-jcb-50 border-b-2 border-jcb-400 border-opacity-0 hover:border-opacity-100 hover:text-jcb-200 duration-200 cursor-pointer">
						<a href="">Contribute</a>
					</li>
				</ul>
			</nav>
		</header>
	)

}

export default Header
