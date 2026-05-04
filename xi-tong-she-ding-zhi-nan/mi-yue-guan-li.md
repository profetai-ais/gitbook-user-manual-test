---
description: 本頁面用於集中管理系統所需的密鑰（API Key）。透過此頁可新增、檢視與刪除密鑰，確保系統服務能安全且正確地運作。
---

# 密鑰管理

## 頁面導覽

進入「Key Management」頁面後，畫面會顯示目前已建立的密鑰清單，欄位說明如下：

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="210">名稱</th><th>說明</th></tr></thead><tbody><tr><td>Type</td><td>密鑰類型（例如 SERPER、LiteLLM），代表此金鑰所對應的服務種類</td></tr><tr><td>Name</td><td>密鑰名稱，用於識別此 API Key 的用途</td></tr><tr><td>Key</td><td>API Key 值，為安全考量僅以遮罩方式顯示</td></tr><tr><td>Tenant ID</td><td>所屬租戶識別碼</td></tr><tr><td>Expire Date</td><td>密鑰到期時</td></tr><tr><td>Creator</td><td>建立者</td></tr><tr><td>Created Date</td><td>建立時間</td></tr><tr><td>Modified Date</td><td>最後更新時間</td></tr><tr><td>Actions</td><td>操作功能，目前提供刪除（垃圾桶圖示）</td></tr></tbody></table>

## 新增密鑰

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

1. 點擊右上角「+」後，會開啟新增密鑰的設定視窗，請依序完成以下設定：
2. Type：選擇密鑰類型。
3. Name：輸入此 API Key 的識別名稱，建議填寫具體用途（例如：`litellm api key`），以利後續管理。
4. API Key：輸入實際的 API 金鑰內容。
   * 欄位預設為隱藏顯示
   * 可透過右側「眼睛」圖示切換顯示 / 隱藏
5. 確認送出：設定完成後，點擊 「Ok」 以儲存密鑰；若不儲存則可點擊 「取消」 取消操作。

## 刪除密鑰

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

1. 點擊該列最右側 Actions 欄位中的 垃圾桶圖示
2. 點選確認後執行刪除動作，該密鑰會立即從清單中移除

### **注意事項**

* **刪除後的密鑰無法復原**
* 若該 API Key 正被系統或流程使用中，刪除後可能導致相關功能無法正常運作
* 建議在刪除前，先確認該金鑰已不再被任何服務或流程引用
