const user = { username: 'funguy37', status: 'active' };
const loginStatus = login(user);
console.log(loginStatus);
console.log(`The status is now ${user.status}`);
function login(userCredentials) {
  if (userCredentials.status === 'active') {
    let randomString = Math.random().toString(36).slice(-16);
    userCredentials.status = randomString;
    return `Status was updated.`;
  }
  return 'Logged In';
}
