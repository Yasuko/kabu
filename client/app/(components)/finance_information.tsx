import React from 'react'

import ToolTip from './tooltip'

export default function FinanceInformation({
    info,
}: {
    info: any,
}) {
    return (

    <div className="p-2 md:p-5">
    <div className="flex items-center gap-x-2">
        <p className="text-xs uppercase tracking-wide text-gray-500 dark:text-neutral-500">
            Information
        </p>
    </div>

    <div className="mt-1 flex items-center gap-x-2">
        <div className="flex flex-col">
            <div className="-m-1.5 overflow-x-auto">
                <div className="p-1.5 min-w-full inline-block align-middle">
                <div className="overflow-hidden">
                    <table className="min-w-full divide-y divide-gray-200 dark:divide-neutral-700">
                    <thead>
                        <tr>
                        <th 
                            scope="col"
                            className="px-2 py-3 text-start text-xs font-medium text-gray-500 uppercase dark:text-neutral-500">
                                Info
                        </th>
                        <th
                            scope="col"
                            className="px-2 py-3 text-start text-xs font-medium text-gray-500 uppercase dark:text-neutral-500">
                                Score
                        </th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-200 dark:divide-neutral-700">
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                cursor-pointer
                            ">
                            <ToolTip label="4半期株価" tips={'aaaa'} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.dividendrate * info.trailingeps}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                cursor-pointer
                            ">
                            <ToolTip label="予想株価" tips={'aaaa'} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.dividendrate * info.forwardeps}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                cursor-pointer
                            ">
                            <ToolTip label="DividendRate" tips={docs.dividendRate} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.dividendyield}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                cursor-pointer
                            ">
                            <ToolTip label="DividendYield" tips={docs.dividendYield} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.dividendyield}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="Beta" tips={docs.beta} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.beta}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="ProfitMargins" tips={docs.profitMargins} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.profitmargins}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="PriceToBook" tips={docs.priceToBook} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.pricetobook}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="EnterPriseToEbitda" tips={docs.enterprisetoebitda} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.enterprisetoebitda}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="EnterPriseToRevenue" tips={docs.enterprisetorevenue} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.enterprisetorevenue}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="QuickRatio" tips={docs.quickratio} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.quickratio}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="CurrentRatio" tips={docs.currentratio} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.currentratio}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="DebtToEquity" tips={docs.debttoequity} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.debttoequity}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="ReturnOnAssets" tips={docs.returnonassets} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.returnonassets}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="ReturnOnEquity" tips={docs.returnonequity} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.returnonequity}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="RevenueGrowth" tips={docs.revenuegrowth} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.revenuegrowth}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="GrossMargins" tips={docs.grossmargins} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.grossmargins}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="EbitdaMargins" tips={docs.ebitdamargins} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.ebitdamargins}
                        </td>
                        </tr>
                        <tr>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm font-medium text-gray-800
                                dark:text-neutral-200
                                ">
                                <ToolTip label="OperatingMargins" tips={docs.operatingmargins} position='top' />
                        </td>
                        <td
                            className="
                                px-2 py-2 whitespace-nowrap
                                text-sm text-gray-800 dark:text-neutral-200
                            ">
                                {info.operatingmargins}
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </div>
                </div>
            </div>
        </div>
    </div>
    </div>
    
    )
}


const docs = {
    dividendRate: `
配当利率とは

株価に対する年間配当金の割合を示す指標。

一株当たりの年間配当金を、現在の株価で割って求める。
たとえば、現在株価が1,000円で、配当金が年10円であった場合
配当利回りは1％（10円÷1,000円）となる。

なお、投資をするときは
年間配当金の予想値で計算し、判断材料とする。
    `,
    dividendYield: `
配当利回りとは

企業の年間配当額を現在の株価に対する割合で示したもの。

したがって、株価が下がると、配当利回りは上がることになる。

例えば、株価が１株20ドルで１株配が１ドルなら、配当利回りは５％となるが、
株価が10ドルに値下がりすると、配当利回りは10％になる。

バリュー投資家はよく、配当利回りの高さを割安株の目安にしているが
配当利回りが高いと、リスクを嫌う投資家には魅力的に映るため
下げ相場でもクッションの役目を果たすことになる。

ただし、マイナス面としては、配当には通常の所得税が課せられるため
高利回りになるほど、税金を多く支払わなければいけなくなる。 
    `,
    beta: `
ベータ値（β）とは

株式市場のインデックスと個別企業の株価の相関関係を示す指標で
株式のリスク尺度として用いられます。

ベータ値は、株式市場の動きを1とした場合
その企業の株価がどの程度変化するかを数値化したもので

次のような意味があります。

* β値が1の場合、株式市場全体の動きと等しく株価が上下動します。
 
* β値が1より大きい場合、市場全体に比べて値動きが大きく
  相場変動に対するリスクが高くなります。
* β値が0の場合、株価は市場の動きとは無関係に動くことを意味します。
* β値がマイナスに転じると市場とは逆の変動をすることを意味します。

ベータ値は、過去の個別銘柄の株価と市場全体の値動きの相関
（期間はおおむね2年から3年程度）から求められます。
現代のポートフォリオ理論ではよく用いられる言葉で
市場全体が上昇すると判断する場合は
β値の高い銘柄に投資したり、ポートフォリオ全体のβ値を「1」として
市場全体と連動させるなどの運用を行う際、銘柄選択に用いられます。
    `,
    profitMargins: `
Profit margin（プロフィットマージン）とは

企業の利益を売上高で割った利益率を指します。

通常はパーセンテージで表され

計算式は「profit margin =（利益÷売上げ）× 100」です。

企業の収益性を表す経営指標には、次のようなものもあります。

売上高総利益率（粗利益率）：
販売している商品の利益率を示す比率で
景気が良いときは上昇し、不景気になると下落します。

業種によって差があり
製造業で15～60％
小売業で20～30％
商社では1.5～2.0％程度です。

オペレーティングマージン：
売上総利益に対する営業利益の割合を表す経営指標です。
会計基準が異なる企業同士でも収益力を比較することができます。
売上高営業利益率：本来の営業活動による利益率で
本業の収益性が高いかどうかを示します。
同業他社と比較することで
販売活動や管理活動の効率性を知ることができます。
    `,
    priceToBook: `
Price to Book（P/B）とは

株価純資産倍率（PBR）のことで
株価が1株あたりの純資産に対して
割安か割高かを判断するための指標です。

PBRは、株価を1株あたりの純資産で割って求める数値で
単位は「倍」です。
PBRが高いほど株価が純資産に対して
高く評価されている（割高）ことを表し
PBRが低いほど、株価が純資産に対して
低く評価されている（割安）ことを示します。

PBRの目安は一般的に1倍とされており、PBRが1倍であれば
株価と企業の資産価値が釣り合っていると考えられます。

PBRが1倍を下回る「PBR1倍割れ」の場合
その企業の株価は割安と捉えられます。

PBRは株価の水準を判断する代表的な指標の1つで
企業の資産内容や財務状態をもとに株価水準を測る指標です。
    `,
    trailingEps: `
Trailing EPS（Trailing Earnings Per Share）とは

企業の過去4四半期の利益（earnings）を積み上げた
1株あたりの利益（per share）を指します。

企業の収益性を示す指標として広く用いられていますが
過去の状況を示すもので、将来の予測には使用できません。

将来の利益を予測するには、過去のEPSの値を基にモデルを適用したり
業績の見通しを考慮したりします。
    `,
    forwardEps: `
Forward EPS（フォワードEPS）とは

今後12ヶ月間の予想される1株当たり純利益（EPS）です。

EPS（Earnings Per Share）は、企業の当期純利益を株式数で割ったもので
企業の収益性を測る指標です。

EPSの値が高い企業ほど収益性が高く
投資家にとって魅力的な投資先と判断されることが多くなっています。
    `,
    pegRatio: `
PEGレシオ（Price Earnings Growth Ratio）とは
企業の株価収益率（PER）と企業の利益成長率を加味して
企業価値を測る指標です。

PEGレシオは、予想株価収益率（PER）を
1株当たりの予想利益成長率で割って算出されます。
一般的に、PEGレシオが1倍以下なら割安
2倍以上なら割高と判断されます。
PEGレシオは、PERが高い銘柄や成長企業の株価の割安性を
判断するために主に使われます。
企業の成長性（Growth）も加味した指標であるため
企業の成長に市場の焦点が当たる局面では
PERよりもPEGレシオの効果が上回ると考えられます。
    `,
    enterprisetorevenue: `
Enterprise to revenue（EV/R）とは

企業価値（Enterprise Value）を
売上高（Revenue）で割って算出する倍率で
企業の収益と企業価値を比較する指標です。

EV/Rは、投資家が株価が適正に評価されているかどうかを
判断する際に使用される指標の1つで
企業の評価を行う場合にも用いられます。

EV/Rの値が低いほど企業が過小評価されている可能性があり
企業の収益と企業価値が比較されることで、企業の業績や成長性
競争力などを理解する助けになります。

EV/Rの計算式は「企業価値（EV） / 売上高」です。

企業価値（EV）は、企業を買収する際に必要な実質的な資金の額で
買収に要する時価総額と買収後に返済する必要がある金額の合計です。

ただし、EV/Rは同じ業界の企業同士を比較して算出するため
どの企業が業界で最も優れているのかを判断することは困難です。

また、EV/Rの算出には市場株価と比べてより多くの計算が必要なため
業界内のすべての競合企業に対してEV/Rを算出することは時間がかかります。
    `,
    enterprisetoebitda: `
Enterprise to EBITDA（イーブイ/イービッダー）とは

企業の事業価値（Enterprise Value：EV）が
本業の利益（EBITDA）の何倍かを表す指標です。

簡易買収倍率とも呼ばれ、M&Aの際に企業の価値や
将来収益力を分析する際に用いられます。

EV/EBITDA倍率の計算式は「EV/EBITDA倍率＝EV÷EBITDA」です。

EVは企業の株式時価総額と
ネット有利子負債（有利子負債-非事業用資産）で算出され
EBITDAは「利払い前税引き前償却前利益」を意味します。

EV/EBITDA倍率は、企業の買収に必要な時価総額と
買収後の純負債の返済に必要な金額を
EBITDAの何年分で賄えるかを表します。

EV/EBITDA倍率が低いほど
買収により高い成果があると判断できます。

EV/EBITDA倍率の目安は一般的に8倍といわれていますが
成長期にある業種やベンチャー企業などの場合は
3倍から8倍の間になることが多く
8年での投資回収は割高であると判断される場合があります。
    `,
    quickratio: `
Quick Ratio（クイック比率）には、次のような意味があります。

企業の短期的な支払能力を分析する指標で、当座比率とも呼ばれる

サブスクリプション型のサービスとして展開するSaaSビジネスにおいて
一定期間に獲得した収益と同期間の損失の比率を表すKPI

Quick Ratioは、企業の当座資産を流動負債で除して求めます。

当座資産と流動負債を対比することで
企業の支払能力を判定する指標です。

Quick Ratioの目安は、一般的に100％以上
あるいは1回転以上と言われています。
この比率が50％、あるいは0.5を下回ると流動性が低くなり
資金繰りが厳しくなるといわれています。
また、Quick RatioはSaaSビジネスにおいて
ビジネスの健全性を可視化する評価項目として設定されることが多く
成長効率の測定値としても使用されます。
    `,
    currentratio: `
Current ratio（流動比率）とは
企業の短期的な支払能力や財務体質の健全性を評価する指標です。
流動資産を流動負債で割った比率で、1年以内に支払期限の到来する負債に対して
1年以内に現金化できる資産がどの程度あるのかを分析しています。
流動比率の目安は、国内では一般的に150%以上とされています。

100%を下回ると支払い能力に不安があると考えられ
近いうちに資金がショートして会社が倒産するリスクがあることを意味しています。
流動比率の計算式はシンプルですが、流動資産の内容に注意する必要があります。
流動資産とは、1年以内に現金化される見込みのある資産ですが
計上した流動資産のすべてが1年以内に現金化されるとは限りません。

流動比率と似た指標に当座比率がありますが
当座比率は棚卸資産のような換金性の低い資産は資産に含まれないことが多いです。
当座比率は、流動比率よりも短い数ヶ月という期間での支払い能力を把握するための指標です。
    `,
    debttoequity: `
Debt to Equity Ratio（デット・エクイティ・レシオ）とは
企業の財務健全性を評価する指標で、負債資本倍率とも呼ばれます。
DEレシオは、企業の資金源泉のうち
返済義務のある有利子負債が返済義務のない自己資本の何倍に当たるかを示す数値です。
数値が低いほど財務内容が安定していることを示し
一般的に1倍を下回ると財務が安定しているとされています。
DEレシオの計算式は「負債÷自己資本」です。
DEレシオは、主に長期の支払能力を測る指標として使われ
社債の格付けや金融機関が融資を行う際に使用されます。
DEレシオを低下させるには、負債の削減か
または利益拡大による内部留保の積み増しが必要となります。
    `,
    returnonassets: `
Return on Assets（ROA）とは
総資産利益率のことで、企業の総資産に対する当期純利益の割合を示す財務指標です。
ROAは、企業が自社の総資産をいかに効率的に活用できているかを判断する指標で
企業全体の経営効率を測るのに役立ちます。
ROAの数値が高いほど、企業の資産をうまく活用して売上を伸ばしていることを示します。

ROAの計算式は「ROA（％）＝当期純利益÷総資産×100」です。

当期純利益は損益計算書（P/L）に、総資産は貸借対照表（B/S）に記載されています。
ROAは、ROE（自己資本利益率）と並んで、投資家が企業に投資する際に参考にする数値の1つです。
ただし、ROAの数値は業種などによっても異なるため
一概に高いから良い、低いから悪いとも言い切れません。
業種別の平均値を知ることで、企業に求められるROAの目安が分かります。
    `,
    returnonequity: `
Return on Equity（ROE）とは
株主が出資した資金に対する企業の収益性を示す財務指標で
「自己資本利益率」とも呼ばれます。
企業が株主の資本をいかに効率的に活用し、どれだけの利益を上げているかを測る指標です。
ROEの計算式は、次のとおりです。

ROE（％）＝当期純利益 ÷ 自己資本 × 100

ROE（％）＝EPS（一株当たり利益）÷ BPS（一株当たり純資産）× 100

ROEの数値が高いほど、企業が株主資本を有効に利用していることになります。
ROEが高い企業は効率的な経営をしており、低ければ非効率と判断され
企業の株価に大きな差が出てきます。
    `,
    revenuegrowth: `
収益成長率とは
企業の売上高の伸び率を指し、売上高伸び率とも呼ばれます。
企業の成長性や規模の拡大ペースを分析する際に用いられる指標で
社内外で注目される経営指標の1つです。

収益成長率の計算式は「（当期売上高－前期売上高）÷前期売上高」です。

収益成長率が重要である理由は、次のような点です。

* 売上が伸びることで、会社は運営費用を賄い、従業員に給与を支払い
  必要なリソースとテクノロジーに投資することができます。
* 売上の停滞や減少は、人員削減、負債の蓄積
  そして最終的には事業の失敗につながる可能性があります。

ただし、収益成長率が高くても、それが市場の成長率や物価の上昇率を下回っている場合には
実質的な売上高の減少が起きていることを意味するので注意が必要です。
    `,
    grossmargins: `
Gross margin（グロスマージン）とは
売上原価を差し引いた後の収益（粗利益）を総収益のパーセンテージとして表したもので
「売上総利益率」とも呼ばれます。
企業の収益性を判断するための基本的な指標の一つで
この比率が高いほど収益性は高くなります。
Gross margin に関連する用語には、次のようなものがあります。

gross margin improvement：粗利益（売上総利益）の改善
gross margin method：総（利）益法
gross margin on sales：売上総利益
deferred gross margin：繰延総利益
planned gross margin：計画粗利益

ビジネスや会計の文脈で使われることが多く
適切な場面で使い分けることが重要です。
    `,
    ebitdamargins: `
EBITDAマージンとは
企業の収益性を示す指標の1つで、EBITDAを売上高で割った値です。
売上高のうちどの程度が実質的な利益として残るかを表し
企業のコスト管理や運営効率の評価に使用されます。
EBITDAマージンは、次のような特徴があります。

減価償却費の影響を除いた企業の収益性を図ることができる。

設備投資額が大きい業界や業種の企業分析時に有用とされている。
異なる企業や事業の収益性を比較することができる。
国を超えた同業種の企業の比較も可能になる。
EBITDAマージンが高ければ高いほど収益性の高い事業を営んでいるといえる。

EBITDA（Earnings before Interest, Taxes, Depreciation and Amortization）とは
利払い前・税引き前・減価償却前利益のことです。
簡便には営業利益に減価償却費を加えて計算します。
    `,
    operatingmargins: `
Operating margin（オペレーティングマージン）とは
売上総利益に対する営業利益の割合を表す経営指標です。
営業利益率とも呼ばれます。

Operating marginは、会計基準が異なる企業同士でも収益力を比較する際に有効です。

Operating marginの計算式は、営業利益を売上高で割り、100を掛け算します。

営業利益は、英語で「Operating profit」と表現されます。
損益計算書では、まず売上高から売上原価を差し引いて売上総利益を計算し
そこからさらに販売費および一般管理費を控除した残りが営業利益です。
    `,

}