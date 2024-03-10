import React from "react";
import { createRoot } from 'react-dom/client';

const App = () => {
	return (
	  <h2> Hello World </h2>
	);
};

const appDiv = document.getElementById("app");
createRoot(appDiv).render(<App />);