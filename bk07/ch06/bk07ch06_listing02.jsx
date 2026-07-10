import { useState } from 'react';
function Counter(props) {
  const [counter, setCounter] = useState(0);
  function increment() {
    setCounter((prevCount) => prevCount + 1);
  }
  return <button onClick={increment}>{counter}</button>;
}
export default Counter;
