import { render } from 'react-dom';

let MAP_NODE = 'map-root',
    MAP;

if (MAP = document.getElementById(MAP_NODE)) {
    import('./map.js')
        .then(MapRoot => {
            render(MAP, MapRoot)
        });
}
