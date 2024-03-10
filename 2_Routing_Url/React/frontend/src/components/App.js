import React from "react";
import { createRoot } from 'react-dom/client';
import RoutesComponent from './RoutesComponent';

const App = () => {
	return (
		<div>
			<RoutesComponent />
		</div>
	);
};

const appDiv = document.getElementById("app");
createRoot(appDiv).render(<App />);