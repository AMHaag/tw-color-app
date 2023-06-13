export interface Palette {
  shades: {
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
    shade950: string;
  };
}

export default function ColorPalette({ shades }: Palette) {
  const swatches = [];

  for (const [key, value] of Object.entries(shades)) {
    const swatchClass = `h-16 w-96 flex justify-between items-center xl:flex-col xl:h-72 hover:drop-shadow-xl `;
    swatches.push(
      <div className={swatchClass} style={{ backgroundColor: value }}>
        <div className="mx-3 rounded-xl bg-[hsla(217,100%,0%,0.2)] xl:my-3">
          <p className="mx-3 w-10 p-1  text-center font-stencil text-white ">
            {key.replace(/\D/g, "")}
          </p>
        </div>
        <div className="mx-3 rounded-xl bg-[hsla(217,100%,0%,0.2)] xl:my-3">
          <p className="mx-3 w-16 p-1 text-center font-stencil text-white">
            {value}
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="m-5 my-4  flex flex-col items-center rounded-xl xl:flex-row">
      {swatches}
    </div>
  );
}
