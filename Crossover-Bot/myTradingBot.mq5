#include<Trade\Trade.mqh>
CTrade trade;

string signal;
double tradePrice;

void OnTick()
{
   double ask = NormalizeDouble(SymbolInfoDouble(_Symbol, SYMBOL_ASK), _Digits);
   double bid = NormalizeDouble(SymbolInfoDouble(_Symbol, SYMBOL_BID), _Digits);
   
   //price data
   MqlRates priceInfo[];
   int priceData = CopyRates(Symbol(), _Period, 0, 3, priceInfo);
   
   //array for several prices
   double big[];
   double med[];
   double small[];
   
   ArraySetAsSeries(big, true);
   ArraySetAsSeries(med, true);
   ArraySetAsSeries(small, true);
   
   int bigDef = iMA(_Symbol, _Period, 5, 0, MODE_EMA, PRICE_CLOSE);
   int medDef = iMA(_Symbol, _Period, 20, 0, MODE_EMA, PRICE_CLOSE);
   int smallDef = iMA(_Symbol, _Period, 50, 0, MODE_EMA, PRICE_CLOSE);
   
   CopyBuffer(bigDef, 0, 0, 3, big);
   CopyBuffer(medDef, 0, 0, 3, med);
   CopyBuffer(smallDef, 0, 0, 3, small);
   
   //Buy signal 
   if((med[0] < small[0]) && (med[1] > small[1]) && (PositionsTotal() < 1)){
      if((small[0] > big[0]) && (med[0] > big[0]) && (priceInfo[0].close > big[0])){
         
         signal = "buy";
         tradePrice = ask;
         TradeLong(ask);
      }
   }
   //Sell Signal
   if((med[0] > small[0]) && (med[1] < small[1]) && (PositionsTotal() < 1)){
      if((small[0] < big[0]) && (med[0] < big[0]) && (priceInfo[0].close < big[0])){
         
         signal = "sell";
         tradePrice = bid;
         TradeShort(bid);
      }
   }
   
   if(PositionsTotal() > 0 && signal == "buy"){
   
      if(priceInfo[0].close > (tradePrice + 50 * _Point)){
      
         trade.PositionModify(PositionGetTicket(0), tradePrice, PositionGetDouble(POSITION_TP));
      }
   }
   
   if(PositionsTotal() > 0 && signal == "sell"){
   
      if(priceInfo[0].close < (tradePrice - 50 * _Point)){
      
         trade.PositionModify(PositionGetTicket(0), tradePrice, PositionGetDouble(POSITION_TP));
      }   
   }
   
   Comment("Price: ", tradePrice);   
}

void TradeLong(double ask){
   
   if (PositionsTotal() < 1){
      
      trade.Buy(0.01, NULL, ask, ask - 50 * _Point, ask + 100 * _Point, NULL);
   } 
   //chart output
   Comment("Signal: ", signal);
}

void TradeShort(double bid){
   if (PositionsTotal() < 1){
      
      trade.Sell(0.01, NULL, bid, bid + 50 * _Point, bid - 100 * _Point, NULL);
   } 
   //chart output
   Comment("Signal: ", signal);
}