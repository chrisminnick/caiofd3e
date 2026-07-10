import Message from './bk07ch04_listing03.jsx';
function WelcomeScreen() {
  const header = (
    <h1>
      <Message message="Welcome!" messageType="header" />
    </h1>
  );
  return header;
}
export default WelcomeScreen;
