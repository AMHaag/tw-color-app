import SearchBar from './components/searchbar'
import ColorPalette from './components/colorPalette'
import test_palette from '../utils/test_palette.json'
export default function Page() {
	
	return (
		<div className=''>
			<SearchBar />
			<ColorPalette shades={test_palette}/>
		</div>
	)
}
