import { useState } from "react";
import ContentsBlock from "./ContentsBlock";

export default function ContentsSelector({ onChange }) {
  const [selectedBlocks, setSelectedBlocks] = useState([]);

  // 부모(Dashboard)로 값 전달
  const handleChange = (name, label) => {
    setSelectedBlocks((prev) => {
      let updated;
      if (prev.some((b) => b.name === name)) {
        updated = prev.filter((b) => b.name !== name);
      } else {
        updated = [...prev, { name, label }];
      }

      if (onChange) {
        const names = updated.map((b) => b.name); // API용
        const labels = updated.map((b) => b.label); // UI용
        onChange(names, labels);
      }
      return updated;
    });
  };

  return (
    <div className="mt-2 flex grid-cols-4 flex-wrap gap-2">
      <ContentsBlock
        name="headline"
        label="📰 헤드라인 뉴스"
        active={selectedBlocks.some((b) => b.name === "headline")}
        onClick={handleChange}
      />
      <ContentsBlock
        name="deep"
        label="🔎 심층 뉴스"
        active={selectedBlocks.some((b) => b.name === "deep")}
        onClick={handleChange}
      />
      <ContentsBlock
        name="current"
        label="🗞️ 추가 뉴스"
        active={selectedBlocks.some((b) => b.name === "current")}
        onClick={handleChange}
      />
      <ContentsBlock
        name="story"
        label="🎙️ 사연"
        active={selectedBlocks.some((b) => b.name === "story")}
        onClick={handleChange}
      />
      <ContentsBlock
        name="music"
        label="🎶 음악 이슈"
        active={selectedBlocks.some((b) => b.name === "music")}
        onClick={handleChange}
      />
    </div>
  );
}
