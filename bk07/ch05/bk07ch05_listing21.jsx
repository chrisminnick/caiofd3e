import { Blink, SolidBorderBox } from './bk07ch05_listing20.jsx';
function App() {
  return (
    <SolidBorderBox>
      <Blink delay={1000}>
        <p>Important Message</p>
      </Blink>
    </SolidBorderBox>
  );
}
export default App;
