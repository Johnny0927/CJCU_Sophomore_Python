import java.util.Scanner;

public class main{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		
		while(sc.hasNext()){
			long s = sc.nextLong();
			long d = sc.nextLong();

            while(d > 0){
                d -= s;
                s++;
            }

			System.out.println(s-1);
		}
	}
}