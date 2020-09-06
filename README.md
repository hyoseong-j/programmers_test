# programmers_test
## 코딩 단어 정리

1. str.[isdigit()](https://docs.python.org/ko/3/library/stdtypes.html?highlight=isdigit#str.isdigit) : check the num
 
 ``` 
 ex1)
 input -> "1234"
 output -> True
 ex2)
 input -> "abc"
 output -> False
 ```
 
 2. str.[isalpha()](https://docs.python.org/ko/3/library/stdtypes.html?highlight=isalpha#str.isalpha) : check the char
 
 ```
 ex1)
 input -> "1234"
 output -> False
 ex2)
 inputt -> "abc"
 output -> True
 ```
 
 <table class="docutils align-default" id="index-19">
<colgroup>
<col style="width: 38%">
<col style="width: 47%">
<col style="width: 15%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>연산</p></th>
<th class="head"><p>결과</p></th>
<th class="head"><p>노트</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">x</span> <span class="pre">in</span> <span class="pre">s</span></code></p></td>
<td><p><em>s</em> 의 항목 중 하나가 <em>x</em> 와 같으면 <code class="docutils literal notranslate"><span class="pre">True</span></code>, 그렇지 않으면 <code class="docutils literal notranslate"><span class="pre">False</span></code></p></td>
<td><p>(1)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">x</span> <span class="pre">not</span> <span class="pre">in</span> <span class="pre">s</span></code></p></td>
<td><p><em>s</em> 의 항목 중 하나가 <em>x</em> 와 같으면 <code class="docutils literal notranslate"><span class="pre">False</span></code>, 그렇지 않으면 <code class="docutils literal notranslate"><span class="pre">True</span></code></p></td>
<td><p>(1)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s</span> <span class="pre">+</span> <span class="pre">t</span></code></p></td>
<td><p><em>s</em> 와 <em>t</em> 의 이어 붙이기</p></td>
<td><p>(6)(7)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s</span> <span class="pre">*</span> <span class="pre">n</span></code> 또는 <code class="docutils literal notranslate"><span class="pre">n</span> <span class="pre">*</span> <span class="pre">s</span></code></p></td>
<td><p><em>s</em> 를 그 자신에 <em>n</em> 번 더하는 것과 같습니다</p></td>
<td><p>(2)(7)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s[i]</span></code></p></td>
<td><p><em>s</em> 의 <em>i</em> 번째 항목, 0에서 시작합니다</p></td>
<td><p>(3)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s[i:j]</span></code></p></td>
<td><p><em>s</em> 의 <em>i</em> 에서 <em>j</em> 까지의 슬라이스</p></td>
<td><p>(3)(4)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s[i:j:k]</span></code></p></td>
<td><p><em>s</em> 의 <em>i</em> 에서 <em>j</em> 까지 스텝 <em>k</em> 의 슬라이스</p></td>
<td><p>(3)(5)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">len(s)</span></code></p></td>
<td><p><em>s</em> 의 길이</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">min(s)</span></code></p></td>
<td><p><em>s</em> 의 가장 작은 항목</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">max(s)</span></code></p></td>
<td><p><em>s</em> 의 가장 큰 항목</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s.index(x[,</span> <span class="pre">i[,</span> <span class="pre">j]])</span></code></p></td>
<td><p>(인덱스 <em>i</em> 또는 그 이후에, 인덱스 <em>j</em> 전에 등장하는) <em>s</em> 의 첫 번째 <em>x</em> 의 인덱스</p></td>
<td><p>(8)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s.count(x)</span></code></p></td>
<td><p><em>s</em> 등장하는 <em>x</em> 의 총수</p></td>
<td></td>
</tr>
</tbody>
</table>
     
