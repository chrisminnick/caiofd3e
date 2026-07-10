import { useState } from 'react';
function Counter(props) {
  const [counter, setCounter] = useState(0);
  function increment(incrementBy = 1) {
    setCounter(counter + incrementBy);
  }
  return <button onClick={() => increment(2)}>Add 2</button>;
}
export default Counter;
