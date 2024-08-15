import { useEffect, useState } from "react";
import Navbar from "./Components/Navbar/Navbar";
import "./index.css";
function App() {
  const [theme, setTheme] = useState<string>(
    localStorage.getItem("theme") || "light"
  );
  const element = document.documentElement;
  useEffect(() => {
    if (theme === "dark") {
      element.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      element.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  }, [theme]);
  return (
    <div className="bg-white dark:bg-black dark:text-white">
      <Navbar theme={theme} setTheme={setTheme} />
    </div>
  );
}

export default App;
