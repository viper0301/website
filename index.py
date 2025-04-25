export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50 text-gray-800 p-8 space-y-12">
      {/* 1. 個人簡介 */}
      <section className="max-w-3xl mx-auto">
        <h1 className="text-4xl font-bold mb-4">嗨，我是小明</h1>
        <p className="text-lg leading-relaxed">
          根據我的職涯測驗（104興趣何倫碼），我屬於 R（實用型）和 I（研究型），對資訊系統、邏輯分析與問題解決有高度興趣。
          我具備良好的邏輯推理能力，熱愛使用科技工具提升工作效率。
        </p>
      </section>

      {/* 2. 工作介紹 */}
      <section className="max-w-3xl mx-auto">
        <h2 className="text-2xl font-semibold mb-2">應徵職缺：資訊管理師 - 台灣某科技公司</h2>
        <ul className="list-disc pl-6 text-base space-y-1">
          <li>公司名稱：ABC科技股份有限公司</li>
          <li>工作地點：台北市內湖區</li>
          <li>工作內容：資訊系統維護、資料分析、ERP系統導入與使用者支援</li>
          <li>需求條件：具MIS或資管背景，熟悉SQL、Python、ERP佳</li>
        </ul>
      </section>

      {/* 3. 自傳履歷 */}
      <section className="max-w-3xl mx-auto">
        <h2 className="text-2xl font-semibold mb-2">自傳履歷</h2>
        <p className="text-base leading-relaxed space-y-2">
          我從大學主修資訊管理系，累積了豐富的系統設計與資料處理知識。曾在校內專題中開發小型ERP模組，並參與資料視覺化分析專案。
          我有良好的溝通能力與團隊合作經驗，能快速理解使用者需求並轉化為可執行的技術方案。對於ABC科技的職缺非常有熱情，
          希望能加入團隊，協助提升資訊系統效率，創造更多價值。
        </p>
      </section>

      {/* 4. 聯絡方式 */}
      <section className="max-w-3xl mx-auto">
        <h2 className="text-2xl font-semibold mb-2">聯絡方式</h2>
        <p>Email：mingjob@gmail.com</p>
        <p>LinkedIn：linkedin.com/in/ming</p>
      </section>
    </main>
  );
}
