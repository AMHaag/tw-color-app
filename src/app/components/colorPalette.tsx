


export interface Palette {
		shades:{
		shade50: string;
		shade100: string;
		shade200: string;
		shade300: string;
		shade400: string;
		shade500: string;
		shade600: string;
		shade700: string;
		shade800: string;
		shade900: string;
		shade950: string;}
}



export default function ColorPalette( {shades}:Palette){

	return (
		<div>
			{shades.shade50}
		</div>
	)
}
