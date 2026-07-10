import './App.css';
import useGitHubRepos from './bk07ch05_listing22.jsx';
function App() {
  const [repos, isLoading] = useGitHubRepos('facebook');
  const reposList = repos.map((repo, index) => (
    <li key={index}>
      <a href={repo.clone_url}>{repo.name}</a>
    </li>
  ));
  return <div>{isLoading ? 'Loading…' : reposList}</div>;
}
export default App;
