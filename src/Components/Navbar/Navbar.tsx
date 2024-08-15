const Navbar = () => {
  const Navlinks = [
    {
      id: 1,
      name: "Home",
      link: "/",
    },
    {
      id: 2,
      name: "About",
      link: "/about",
    },
    {
      id: 3,
      name: "How it works",
      link: "/howitworks",
    },
    {
      id: 4,
      name: "Contact",
      link: "/contact",
    },
  ];
  return (
    <nav className="shadow-md bg-gray-200 duration-300">
      <div className="container md:py-0 py-3">
        <div className="flex justify-between">
          <div className="p-5">
            <h1 className="text-2xl font-bold font-serif">Comment Analyser</h1>
          </div>
          <div className="md:block">
            <ul className="flex items-center gap-8">
              {Navlinks.map((data) => (
                <li key={data.id} className="py-4">
                  <a
                    className="inline-block py-2 hover:border-b-2 hover:border-green-600 hover:text-green-400 transition-colors duration-500 text-lg font-medium"
                    href={data.link}
                  >
                    {data.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
