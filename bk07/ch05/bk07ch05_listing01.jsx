export default function Bing() {
  return (
    <Homepage>
      <TopNav />
      <SearchBox />
      <NewsImageScroller />
      <div>
        <div className="leftColumn">
          <TopStories />
        </div>
        <div className="rightColumn">
          <Weather postalCode="97103" />
          <Sports />
        </div>
      </div>
    </Homepage>
  );
}
