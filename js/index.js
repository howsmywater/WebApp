import React from 'react';
import { render } from 'react-dom';

let MAP_NODE = 'map-root',
    MAP;

document.addEventListener("DOMContentLoaded", () => {
    if (MAP = document.getElementById(MAP_NODE)) {
        import('./map')
            .then(({ default: MapRoot }) => {
                render(<MapRoot />, MAP)
            });
    }
});
