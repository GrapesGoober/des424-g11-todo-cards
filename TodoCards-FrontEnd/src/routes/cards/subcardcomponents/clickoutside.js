// copied this code from svelte.dev REPL
// https://svelte.dev/repl/0ace7a508bd843b798ae599940a91783?version=3.16.7

/** Dispatch event on click outside of node */
export function clickOutside(node) {
  
  const handleClick = event => {
    if (node && !node.contains(event.target) && !event.defaultPrevented) {
      node.dispatchEvent(
        new CustomEvent('click_outside', node)
      )
    }
  }

	document.addEventListener('click', handleClick, true);
  
  return {
    destroy() {
      document.removeEventListener('click', handleClick, true);
    }
	}
}