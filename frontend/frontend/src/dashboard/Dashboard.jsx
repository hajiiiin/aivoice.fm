import React, { useState } from 'react';

export default function Dashboard() {
  const [keyword, setKeyword] = useState('');
  const [selectedContents, setSelectedContents] = useState({
    news: false,
    story: false,
    music: false,
  });
  const [storyText, setStoryText] = useState('');

  const handleCheckboxChange = (e) => {
    const { name, checked } = e.target;
    setSelectedContents((prev) => ({ ...prev, [name]: checked }));
  };

  const handleSaveStory = async () => {
    try {
      const res = await fetch('/api/save-story', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ story: storyText }),
      });
      if (res.ok) {
        alert('사연이 저장되었습니다.');
        setStoryText('');
      } else {
        alert('저장 실패');
      }
    } catch (error) {
      console.error('저장 오류:', error);
    }
  };

  return (
    <main style={{ padding: '2rem', maxWidth: '600px', margin: '0 auto' }}>
      <h1>🎙️ AI 라디오 설정</h1>

      <section style={{ marginBottom: '2rem' }}>
        <label>오늘의 키워드: </label>
        <input
          type="text"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          placeholder="예: 가을, 감성, 출근"
          style={{ width: '100%', padding: '8px', marginTop: '8px' }}
        />
      </section>

      <section style={{ marginBottom: '2rem' }}>
        <label>오늘 사용할 콘텐츠:</label>
        <div>
          <label>
            <input
              type="checkbox"
              name="news"
              checked={selectedContents.news}
              onChange={handleCheckboxChange}
            />{' '}
            뉴스
          </label>
          <br />
          <label>
            <input
              type="checkbox"
              name="story"
              checked={selectedContents.story}
              onChange={handleCheckboxChange}
            />{' '}
            사연
          </label>
          <br />
          <label>
            <input
              type="checkbox"
              name="music"
              checked={selectedContents.music}
              onChange={handleCheckboxChange}
            />{' '}
            음악 이슈
          </label>
        </div>
      </section>

      {selectedContents.story && (
        <section style={{ marginBottom: '2rem' }}>
          <label>사연 입력:</label>
          <textarea
            value={storyText}
            onChange={(e) => setStoryText(e.target.value)}
            placeholder="청취자의 사연을 입력하세요"
            rows={6}
            style={{ width: '100%', padding: '8px', marginTop: '8px' }}
          />
          <button onClick={handleSaveStory} style={{ marginTop: '8px' }}>
            사연 저장
          </button>
        </section>
      )}

      <button>라디오 재생</button>
    </main>
  );
}
