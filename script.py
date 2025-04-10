import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

teams_data = {
    'team_name': ['Chennai Super Kings', 'Mumbai Indians', 'Royal Challengers Bangalore', 
                  'Kolkata Knight Riders', 'Delhi Capitals', 'Rajasthan Royals', 
                  'Sunrisers Hyderabad', 'Punjab Kings', 'Gujarat Titans', 'Lucknow Super Giants'],
    'titles': [5, 5, 0, 2, 0, 1, 1, 0, 1, 0],
    'matches_played': [208, 226, 216, 215, 207, 183, 156, 206, 34, 34],
    'matches_won': [121, 129, 107, 113, 97, 95, 78, 95, 22, 17],
    'win_percentage': [58.17, 57.08, 49.54, 52.56, 46.86, 51.91, 50.00, 46.12, 64.71, 50.00],
    'team_colors': ['#FFFF00', '#0080FF', '#FF0000', '#800080', '#0000FF', '#FF69B4', '#FFA500', '#FF0000', '#87CEEB', '#00FFFF']
}

batsmen_data = {
    'player_name': ['Virat Kohli', 'Rohit Sharma', 'MS Dhoni', 'Suryakumar Yadav', 
                    'KL Rahul', 'David Warner', 'AB de Villiers', 'Shikhar Dhawan', 
                    'Chris Gayle', 'Jos Buttler'],
    'team': ['RCB', 'MI', 'CSK', 'MI', 'LSG', 'DC', 'RCB', 'DC', 'PBKS', 'RR'],
    'runs': [7263, 6211, 5082, 2770, 4163, 6201, 5162, 6617, 4965, 2831],
    'innings': [223, 227, 217, 95, 118, 176, 170, 206, 142, 96],
    'average': [37.24, 30.35, 39.09, 32.97, 46.26, 41.89, 40.01, 36.37, 40.04, 35.39],
    'strike_rate': [130.02, 133.81, 135.92, 148.23, 135.33, 140.69, 158.34, 127.38, 148.96, 150.12],
    'fifties': [50, 42, 24, 20, 33, 59, 40, 47, 31, 19],
    'hundreds': [7, 1, 0, 1, 5, 4, 3, 2, 6, 5]
}

teams_df = pd.DataFrame(teams_data)
batsmen_df = pd.DataFrame(batsmen_data)

def set_plot_style():
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.rcParams['axes.edgecolor'] = '#333333'
    plt.rcParams['axes.labelcolor'] = '#333333'
    plt.rcParams['xtick.color'] = '#333333'
    plt.rcParams['ytick.color'] = '#333333'
    plt.rcParams['text.color'] = '#333333'

def visualize_team_success():
    set_plot_style()
    fig, ax = plt.subplots(figsize=(14, 8))
    sorted_df = teams_df.sort_values('win_percentage', ascending=False)
    bars = ax.bar(sorted_df['team_name'], sorted_df['win_percentage'], 
                 color=[c for c in sorted_df['team_colors']], alpha=0.7,
                 label='Win Percentage (%)')
    ax.set_title('IPL Teams Performance Analysis', fontsize=18, pad=20)
    ax.set_xlabel('Team', fontsize=14, labelpad=10)
    ax.set_ylabel('Win Percentage (%)', fontsize=14, labelpad=10)
    ax.tick_params(axis='x', rotation=45, labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.8, 
                f'{height:.1f}%', ha='center', va='bottom', fontsize=10)
    ax2 = ax.twinx()
    ax2.scatter(sorted_df['team_name'], sorted_df['titles'], color='red', 
                s=300, marker='*', label='IPL Titles')
    for i, row in sorted_df.iterrows():
        ax2.text(row['team_name'], row['titles'] + 0.2, 
                str(row['titles']), ha='center', va='bottom', 
                fontweight='bold', fontsize=12, color='darkred')
    ax2.set_ylabel('Number of IPL Titles', fontsize=14, labelpad=15)
    ax2.tick_params(axis='y', labelsize=12)
    ax2.set_ylim(0, max(sorted_df['titles']) + 2)
    ax.legend(loc='upper right')
    ax2.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('ipl_team_performance.png', dpi=300, bbox_inches='tight')
    plt.show()

def visualize_top_batsmen():
    set_plot_style()
    fig, ax = plt.subplots(figsize=(14, 10))
    sorted_df = batsmen_df.sort_values('runs', ascending=False).head(8)
    x = np.arange(len(sorted_df))
    width = 0.2
    ax.bar(x - width, sorted_df['runs']/100, width, label='Runs (hundreds)', 
           color='#3274A1', alpha=0.8)
    ax.bar(x, sorted_df['average'], width, label='Batting Average', 
           color='#E1812C', alpha=0.8)
    ax.bar(x + width, sorted_df['strike_rate']/10, width, label='Strike Rate (÷10)', 
           color='#3A923A', alpha=0.8)
    ax_top = ax.twiny()
    ax_top.set_xlim(ax.get_xlim())
    ax_top.set_xticks(x)
    ax_top.set_xticklabels([f'({row["team"]})' for _, row in sorted_df.iterrows()])
    ax_top.tick_params(axis='x', labelsize=10, pad=0)
    ax.set_xticks(x)
    ax.set_xticklabels(sorted_df['player_name'])
    ax.tick_params(axis='x', rotation=45, labelsize=12, pad=10)
    ax.set_title('Top IPL Batsmen Performance Analysis', fontsize=18, pad=30)
    ax.set_xlabel('Player', fontsize=14, labelpad=15)
    ax.set_ylabel('Performance Metrics', fontsize=14, labelpad=10)
    ax.legend(loc='upper right', fontsize=12)
    for i, (idx, row) in enumerate(sorted_df.iterrows()):
        ax.annotate(f"50s: {row['fifties']}\n100s: {row['hundreds']}", 
                   (i, 5), ha='center', fontsize=10,
                   bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    for i, (idx, row) in enumerate(sorted_df.iterrows()):
        ax.text(i - width, row['runs']/100 + 1, f"{row['runs']}", 
               ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig('ipl_batsmen_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    print("IPL Cricket Stats Visualization")
    print("===============================")
    print("\n1. Team Performance Analysis")
    visualize_team_success()
    print("\n2. Top Batsmen Analysis")
    visualize_top_batsmen()
    print("\nVisualizations completed and saved as PNG files.")

if __name__ == "__main__":
    main()
