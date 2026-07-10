import * as styles from './bk07ch04_listing12.js';
function Article({ headline, authorName, bodyText }) {
  return (
    <div>
      <h2 style={styles.headline}>{headline}</h2>
      <div style={styles.authorName}>by: {authorName}</div>
      <div style={styles.bodyText}>{bodyText}</div>
    </div>
  );
}
export default Article;
